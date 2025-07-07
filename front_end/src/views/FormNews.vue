<script setup>
import Editor from "primevue/editor";
import { ref } from "vue";

let title = ref("");
let content = ref("");
let imageUrl = ref("");

async function onFormSubmit() {
    try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/news`, {
            method: "POST",
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
            throw new Error("Failed to add news");
        }

        const data = await response.json();
        console.log("News added successfully:", data);
        title.value = "";
        content.value = "";
        imageUrl.value = "";
    } catch (error) {
        
    }
}
</script>

<template>
    <div class="card">
        <Panel header="Add News" class="">
            <Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
                <div class="flex flex-col gap-1">
                    <label for="title" class="font-semibold">Title</label>
                    <InputText id="title" name="title" v-model="title"/>
                </div>
                <div class="flex flex-col gap-1">
                    <label for="imageUrl" class="font-semibold">Image URL</label>
                    <InputText id="imageUrl" v-model="imageUrl" placeholder="Paste image URL here" />
                    <div v-if="imageUrl" class="mt-2">
                        <img :src="imageUrl" alt="Preview" style="max-width: 300px; max-height: 200px;" />
                    </div>
                </div>
                <div class="flex flex-col gap-1">
                    <label for="content" class="font-semibold">Content</label>
                    <Editor name="content" editorStyle="height: 320px" v-model="content"/>
                </div>
                <Button type="submit" severity="primary" label="Submit" />
            </Form>
        </Panel>
    </div>
</template>