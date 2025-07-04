<script setup>
import { ref, onMounted } from "vue";

const news = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const res = await fetch("http://localhost:8000/news");
    news.value = await res.json();
  } catch (e) {
    news.value = [];
  } finally {
    loading.value = false;
  }
});
console.log(news)
</script>

<template>
  <div>
    <h2>News</h2>
    <div v-if="loading">Loading...</div>
    <ul v-else>
      <li v-for="item in news" :key="item.id">
        <strong>{{ item.title }}</strong>
        <div>{{ item.date }}</div>
        <div>{{ item.authors }}</div>
      </li>
    </ul>
  </div>
</template>