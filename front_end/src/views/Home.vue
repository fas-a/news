<script setup>
import StatsWidget from "../components/dashboard/StatsWidget.vue";
import SalesTrendWidget from "../components/dashboard/SalesTrendWidget.vue";
import RecentActivityWidget from "../components/dashboard/RecentActivityWidget.vue";
import ProductOverviewWidget from "../components/dashboard/ProductOverviewWidget.vue";
</script>

<template>
  <div class="layout-grid">
    <StatsWidget />
    <div class="layout-grid-row">
      <SalesTrendWidget />
      <RecentActivityWidget />
    </div>
    <ProductOverviewWidget />
  </div>
</template>
