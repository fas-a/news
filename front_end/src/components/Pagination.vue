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
</script>

<template>
  <div class="pagination">
    <button :disabled="page === 1" @click="prev">Prev</button>
    <span>Page {{ page }} of {{ totalPage }}</span>
    <button :disabled="page === totalPage" @click="next">Next</button>
  </div>
</template>