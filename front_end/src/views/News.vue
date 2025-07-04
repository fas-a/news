<script setup>
import { ref, onMounted } from "vue";
import ProgressSpinner from "primevue/progressspinner";
import NewsCard from "../components/news/NewsCard.vue";
import Pagination from "../components/Pagination.vue";

const news = ref([]);
const loading = ref(true);
const page = ref(1);
const limit = ref(10);
const total = ref(0);

async function fetchNews() {
  loading.value = true;
  try {
    const res = await fetch(`http://localhost:8000/news?skip=${(page.value - 1) * limit.value}&limit=${limit.value}`);
    news.value = await res.json();
    const countRes = await fetch("http://localhost:8000/news/count");
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
</script>

<template>
  <div class="layout-grid">
    <div v-if="loading" class="loading-container">
      <ProgressSpinner
        style="width: 50px; height: 50px"
        strokeWidth="4"
        animationDuration=".8s"
        aria-label="Loading"
      />
      <div class="loading-text">Loading news...</div>
    </div>
    <div v-else>
      <div class="news-grid">
        <NewsCard v-for="item in news" :key="item.id" :item="item" />
      </div>
      <Pagination
        :page="page"
        :total="total"
        :limit="limit"
        @change="handlePageChange"
      />
    </div>
  </div>
</template>

<style scoped>
.news-grid {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-top: 2rem;
}
</style>