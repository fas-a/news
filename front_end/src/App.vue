<script setup>
import AppTopbar from "./components/AppTopbar.vue";
import AppFooter from "./components/AppFooter.vue";
import { useRoute } from "vue-router";
import Toast from 'primevue/toast';
let route = useRoute();
</script>

<template>
    <Toast />
    <div class="layout-container">
        <div v-if="route.path !== '/login'" class="layout-grid">
            <AppTopbar />
            <router-view /> 
            <AppFooter />
        </div>
        <div v-else>
            <router-view />
        </div>
    </div>
</template>
