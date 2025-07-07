<script setup>
import Editor from "primevue/editor";
import { ref, watch, computed } from "vue";
import { useRoute } from "vue-router";
import { useToast } from 'primevue/usetoast';
const toast = useToast();

const props = defineProps({
    editNews: {
        type: Object,
        default: null
    }
});

let title = ref("");
let content = ref("");
let imageUrl = ref("");

const route = useRoute();
let isEdit = route.name === "edit-news" || props.editNews !== null;

async function fetchEditNews(id) {
    try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/news/${id}`);
        if (res.ok) {
            const data = await res.json();
            title.value = data.title || "";
            content.value = data.content || "";
            imageUrl.value = data.thumbnail_url || "";
        }
    } catch (e) {

    }
}

watch(
    () => [props.editNews, route.params.id],
    ([editNews, id]) => {
        if (editNews) {
            title.value = editNews.title || "";
            content.value = editNews.content || "";
            imageUrl.value = editNews.thumbnail_url || "";
        } else if (id) {
            fetchEditNews(id);
        }
    },
    { immediate: true }
);

async function onFormSubmit() {
    try {
        const currentEditNews = props.editNews || null;
        const currentIsEdit = route.name === "edit-news" || currentEditNews !== null;
        const editNewsId = currentEditNews && currentEditNews.id
            ? currentEditNews.id
            : route.params.id;

        const method = currentIsEdit ? "PUT" : "POST";
        const url = currentIsEdit && editNewsId
            ? `${import.meta.env.VITE_API_URL}/news/${editNewsId}`
            : `${import.meta.env.VITE_API_URL}/news`;

        const response = await fetch(url, {
            method,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
            body: JSON.stringify({
                title: title.value,
                url: '',
                thumbnail_url: imageUrl.value,
                date: new Date().toISOString(),
                authors: localStorage.getItem("token"),
                content: content.value,
            })
        });
        if (!response.ok) {
            throw new Error("Failed to save news");
        }

        const data = await response.json();
        if (!currentIsEdit) {
            title.value = "";
            content.value = "";
            imageUrl.value = "";
        }
        showSuccess("Success", "Edit news success");
        await new Promise(resolve => setTimeout(resolve, 1500));
        window.location.href = "/admin/news";
    } catch (error) {
      showError("Error", error.message || "An unexpected error occurred");
    }
}
const showError = (message, detail_message) => {
    toast.add({ severity: 'error', summary: message, detail: detail_message, life: 3000 });
};
const showSuccess = (message, detail_message) => {
    toast.add({ severity: 'success', summary: message, detail: detail_message, life: 3000 });
};
</script>

<template>
  <div class="card">
    <Panel :header="isEdit ? 'Edit News' : 'Add News'">
      <Form @submit="onFormSubmit" class="flex flex-col gap-4">
        <div class="flex flex-col gap-1">
          <label for="title" class="font-semibold">Title</label>
          <template v-if="isEdit">
            <InputText id="title" v-model="title" readonly />
          </template>
          <template v-else>
            <InputText id="title" v-model="title" />
          </template>
        </div>
        <div class="flex flex-col gap-1">
          <label for="imageUrl" class="font-semibold">Image URL</label>
          <InputText
            id="imageUrl"
            v-model="imageUrl"
            placeholder="Paste image URL here"
          />
          <div v-if="imageUrl" class="mt-2">
            <img
              :src="imageUrl"
              alt="Preview"
              style="max-width: 300px; max-height: 200px"
            />
          </div>
        </div>
        <div class="flex flex-col gap-1">
          <label for="content" class="font-semibold">Content</label>
          <Editor
            name="content"
            editorStyle="height: 320px"
            v-model="content"
          />
        </div>
        <Button
          type="submit"
          severity="primary"
          :label="isEdit ? 'Update' : 'Submit'"
        />
      </Form>
    </Panel>
  </div>
</template>
