<script setup>
import { ref, onMounted } from "vue";
import Pagination from "../components/Pagination.vue";

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
</script>

<template>
    <div class="card">
        <DataTable :value="news" tableStyle="min-width: 50rem">
            <template #header>
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="text-xl font-bold">News</span>
                    <Button icon="pi pi-plus" label="Add News" class="p-button-success" @click="$router.push('/admin/news/new')" />
                    <Button icon="pi pi-refresh" rounded raised @click="fetchNews" />
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
                    <Button icon="pi pi-trash" class="p-button-danger" @click="$emit('delete', slotProps.data.id)" />
                </template>
            </Column>
        </DataTable>
        <Pagination :total="total" :page="page" :limit="limit" @change="handlePageChange" />
    </div>
</template>
