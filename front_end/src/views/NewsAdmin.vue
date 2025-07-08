<script setup>
import { ref, onMounted } from "vue";
import { useConfirm } from "primevue/useconfirm";
import { useToast } from "primevue/usetoast";
import Pagination from "../components/Pagination.vue";

const confirm = useConfirm();
const toast = useToast();

const showTemplate = (id) => {
    confirm.require({
        group: 'templating',
        header: 'Confirmation',
        message: 'Are you sure want to delete?.',
        icon: 'pi pi-exclamation-circle',
        rejectProps: {
            label: 'Cancel',
            icon: 'pi pi-times',
            outlined: true,
            size: 'small'
        },
        acceptProps: {
            label: 'Save',
            icon: 'pi pi-check',
            size: 'small'
        },
        accept: () => {
            deleteNews(id);
            toast.add({ severity: 'success', summary: 'Success', detail: 'Delete news success', life: 3000 });
        },
        reject: () => {
            toast.add({ severity: 'error', summary: 'Rejected', detail: 'You have rejected', life: 3000 });
        }
    });
};

const news = ref([]);
const loading = ref(true);
const page = ref(1);
const limit = ref(10);
const total = ref(0);

async function fetchNews() {
    loading.value = true;
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/news?skip=${(page.value - 1) * limit.value}&limit=${limit.value}`);
        news.value = await res.json();
        const countRes = await fetch(`${import.meta.env.VITE_API_URL}/news/count`);
        const countData = await countRes.json();
        total.value = countData.count;
    } catch (e) {
        news.value = [];
    } finally {
        loading.value = false;
    }
}

onMounted(fetchNews);

function handlePageChange(p) {
    page.value = p;
    fetchNews();
    window.scrollTo({ top: 0, behavior: "smooth" });
}
function formatDate(dateString) {
    const date = new Date(dateString);
    const wibOffset = 7 * 60;
    const utc = date.getTime() + (date.getTimezoneOffset() * 60000);
    const wibDate = new Date(utc + (wibOffset * 60000));
    const options = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric'
    };
    const formattedDate = wibDate.toLocaleDateString('id-ID', options);
    const hours = wibDate.getHours().toString().padStart(2, '0');
    const minutes = wibDate.getMinutes().toString().padStart(2, '0');
    return `${formattedDate}, ${hours}:${minutes} WIB`;
}

async function deleteNews(id) {
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/news/${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token") || ""}`
            }
        });
        if (res.ok) {
            fetchNews();
        } else {
            alert("Failed to delete news.");
        }
    } catch (e) {
        alert("Error deleting news.");
    }
}
async function scrapNews() {
    toast.add({ severity: 'info', summary: 'Info', detail: 'Sedang mengambil data...', life: 3000 });
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/scrape-news`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token") || ""}`
            }
        });
        if (res.ok) {
            toast.add({ severity: 'success', summary: 'Success', detail: 'Scrap news success', life: 3000 });
            fetchNews();
        } else {
            toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to scrap news', life: 3000 });
        }
    } catch (e) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Error scrapping news', life: 3000 });
    }
}
</script>

<template>
    <ConfirmDialog group="templating">
        <template #message="slotProps">
            <div class="flex flex-col items-center w-full gap-4 border-b border-surface-200 dark:border-surface-700">
                <i :class="slotProps.message.icon" class="!text-6xl text-primary-500"></i>
                <p>{{ slotProps.message.message }}</p>
            </div>
        </template>
    </ConfirmDialog>
    <div class="card">
        <DataTable :value="news" tableStyle="min-width: 50rem">
            <template #header>
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="text-xl font-bold">News</span>
                    <Button icon="pi pi-plus" label="Add News" class="p-button-success" @click="$router.push('/admin/news/new')" />
                    <Button icon="pi pi-download" rounded raised label="Scrap News" @click="scrapNews" />
                </div>
            </template>
            <Column header="Thumbnail">
                <template #body="slotProps">
                    <img :src="slotProps.data.thumbnail_url" :alt="slotProps.data.title" class="w-24 rounded" />
                </template>
            </Column>
            <Column field="title" header="Title"></Column>
            <Column header="Date">
                <template #body="slotProps">
                    {{ formatDate(slotProps.data.date) }}
                </template>
            </Column>
            <Column field="authors" header="Authors"></Column>
            <Column header="Actions">
                <template #body="slotProps">
                    <Button icon="pi pi-pencil" class="mr-2" @click="$router.push(`/admin/news/${slotProps.data.id}/edit`)" />
                    <Button icon="pi pi-trash" class="p-button-danger" @click="showTemplate(slotProps.data.id)" />
                </template>
            </Column>
        </DataTable>
        <Pagination :total="total" :page="page" :limit="limit" @change="handlePageChange" />
    </div>
</template>
