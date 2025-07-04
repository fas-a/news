<script setup>
import { ref, onMounted } from "vue";
import ProgressSpinner from "primevue/progressspinner";

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
function goToPage(p) {
  if (p < 1 || p > Math.ceil(total.value / limit.value)) return;
  page.value = p;
  fetchNews();
}
function topFunction() {
  window.scrollTo({top: 0, behavior: 'smooth'});
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
        <router-link
          v-for="item in news"
          :key="item.id"
          :to="`/news/${item.id}`"
          class="news-card-link"
        >
          <Card class="news-card">
            <template #header>
              <img
                :src="item.thumbnail_url || 'https://primefaces.org/cdn/primevue/images/usercard.png'"
                alt="news thumbnail"
                class="news-thumbnail"
              />
            </template>
            <template #title>
              <div class="card-title">
                {{ item.title }}
              </div>
            </template>
            <template #subtitle> {{ item.date }} | {{ item.authors }} </template>
            <template #content>
              <div class="card-content">
                <p class="m-0 card-snippet">
                  {{ item.content?.slice(0, 300) }}...
                </p>
              </div>
            </template>
          </Card>
        </router-link>
      </div>
      <!-- Pagination Controls -->
      <div class="pagination">
        <button :disabled="page === 1" @click="() => { goToPage(page - 1); topFunction(); }">Prev</button>
        <span>Page {{ page }} of {{ Math.ceil(total / limit) }}</span>
        <button :disabled="page === Math.ceil(total / limit)" @click="() => { goToPage(page + 1); topFunction(); }">Next</button>
      </div>
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
.news-card-link {
  text-decoration: none;
  color: inherit;
  transition: box-shadow 0.2s;
  border-radius: 8px;
}
.news-card-link:hover .news-card {
  box-shadow: 0 4px 24px 0 rgba(0, 0, 0, 0.12);
  cursor: pointer;
}
.news-card {
  width: 100%;
  max-width: none;
  margin: 0;
  display: flex;
  flex-direction: row;
  height: 200px;
  align-items: stretch;
  transition: box-shadow 0.2s;
}
.news-thumbnail {
  width: 220px;
  height: 100%;
  object-fit: cover;
  border-radius: 8px 0 0 8px;
}
.card-title {
  font-size: 1.25rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
}
.card-content {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  height: 100%;
  width: 100%;
}
.card-snippet {
  flex: 1 1 auto;
  margin-bottom: 1rem;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  line-clamp: 4;
  max-height: 5.6em;
}
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 200px;
  gap: 1rem;
}
.loading-text {
  color: var(--primary-color, #2563eb);
  font-weight: 500;
  font-size: 1.1rem;
  letter-spacing: 1px;
}
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  margin: 2rem 0;
}
.pagination button {
  padding: 0.5rem 1.2rem;
  border-radius: 6px;
  border: none;
  background: var(--primary-color, #2563eb);
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s;
}
.pagination button:disabled {
  background: #ccc;
  color: #888;
  cursor: not-allowed;
}
</style>