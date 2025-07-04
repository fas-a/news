<script setup>
defineProps({
  item: Object
});
</script>
<template>
  <router-link :to="`/news/${item.id}`" class="news-card-link">
    <Card class="news-card">
      <template #header>
        <img
          :src="item.thumbnail_url || 'https://primefaces.org/cdn/primevue/images/usercard.png'"
          alt="news thumbnail"
          class="news-thumbnail"
        />
      </template>
      <template #title>
        <div class="card-title">{{ item.title }}</div>
      </template>
      <template #subtitle>
        {{ item.date }} | {{ item.authors }}
      </template>
      <template #content>
        <div class="card-content">
          <p class="m-0 card-snippet">
            {{ item.content?.slice(0, 300) }}...
          </p>
        </div>
      </template>
    </Card>
  </router-link>
</template>
<style scoped>
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
</style>