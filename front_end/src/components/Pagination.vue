<script setup>
import { computed } from "vue";
const props = defineProps({
  page: Number,
  total: Number,
  limit: Number
});
const emit = defineEmits(["change"]);

const totalPage = computed(() => Math.ceil(props.total / props.limit));

function prev() {
  if (props.page > 1) emit("change", props.page - 1);
}
function next() {
  if (props.page < totalPage.value) emit("change", props.page + 1);
}
function goTo(p) {
  if (p !== props.page) emit("change", p);
}

// Generate array halaman (maksimal 5 tombol, dengan ... jika banyak halaman)
const pageNumbers = computed(() => {
  const total = totalPage.value;
  const current = props.page;
  if (total <= 5) {
    return Array.from({ length: total }, (_, i) => i + 1);
  }
  if (current <= 3) {
    return [1, 2, 3, 4, "...", total];
  }
  if (current >= total - 2) {
    return [1, "...", total - 3, total - 2, total - 1, total];
  }
  return [1, "...", current - 1, current, current + 1, "...", total];
});
</script>

<template>
  <div class="pagination">
    <button :disabled="page === 1" @click="prev">Prev</button>
    <template v-for="n in pageNumbers" :key="n">
      <button
        v-if="n !== '...'"
        :class="{ active: n === page }"
        @click="goTo(n)"
        :disabled="n === page"
      >{{ n }}</button>
      <span v-else class="dots">...</span>
    </template>
    <button :disabled="page === totalPage" @click="next">Next</button>
  </div>
</template>

<style scoped>
.pagination {
  display: flex;
  gap: 0.5rem;
  align-items: center;
  justify-content: center;
  margin: 2rem 0;
}
button {
  padding: 0.4rem 1rem;
  border-radius: 6px;
  border: none;
  background-color: var(--p-primary-50);
  color: var(--p-primary-500);
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s;
}
button:disabled {
  background: #ccc;
  color: #888;
  cursor: not-allowed;
}
button.active {
  background: var(--primary-color-text, #fff);
  color: var(--p-primary-500);
  border: 2px solid var(--p-primary-500);
}
button:hover:not(:disabled) {
  background: var(--p-surface-200);
}
.dots {
  padding: 0 0.5rem;
  color: #888;
  font-weight: bold;
}
</style>