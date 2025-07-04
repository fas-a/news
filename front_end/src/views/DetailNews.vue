<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

let route = useRoute();
let id = route.params.id;
let newsDetail = ref(null);

async function fetchNewsDetail() {
  try {
    const res = await fetch(`http://localhost:8000/news/${id}`);
    if (!res.ok) throw new Error("Network response was not ok");
    newsDetail.value = await res.json();
    newsDetail.value.date = formatDate(newsDetail.value.date);
  } catch (error) {
    console.error("Failed to fetch news detail:", error);
  }
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
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
}
onMounted(() => {
    fetchNewsDetail();
    scrollToTop();
});
</script>

<template>
  <div class="layout-grid">
    <div v-if="!newsDetail" class="loading-container">
      <ProgressSpinner
        style="width: 50px; height: 50px"
        strokeWidth="4"
        animationDuration=".8s"
        aria-label="Loading"
      />
      <div class="loading-text">Loading news detail...</div>
    </div>
    <div v-else class="news-detail">
      <Panel :header="newsDetail?.title" class="title-panel">
        <p class="date-author">{{ newsDetail.date }} | {{ newsDetail.authors }}</p>
        <img class="news-image" :src="newsDetail.thumbnail_url" alt="">
        <p class="m-0 text-panel">
          {{ newsDetail?.content }}
        </p>
      </Panel>
    </div>
  </div>
</template>