<script setup>
defineProps({
  item: Object
});
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
        {{ formatDate(item.date) }} | {{ item.authors }}
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

@media (max-width: 768px) {
  .news-card {
    flex-direction: column;
    height: auto;
  }
  .news-thumbnail {
    width: 100%;
    height: 150px;
    border-radius: 8px 8px 0 0;
  }
}
</style>