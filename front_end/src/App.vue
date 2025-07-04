<script setup>
import AppTopbar from "./components/AppTopbar.vue";
import AppFooter from "./components/AppFooter.vue";
</script>

<template>
    <div class="layout-container">
        <AppTopbar />
        <router-view /> 
        <AppFooter />
    </div>
</template>
