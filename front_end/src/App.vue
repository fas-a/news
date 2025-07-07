<script setup>
import AppTopbar from "./components/AppTopbar.vue";
import AppFooter from "./components/AppFooter.vue";
import AppSidebar from "./components/AppSidebar.vue";
import { useRoute } from "vue-router";
import Toast from 'primevue/toast';
let route = useRoute();
</script>

<template>
    <Toast />
    <div v-if="route.path.includes('/admin')" class="layout-wrapper">
        <AppSidebar class="fixed top-0 left-0 z-40 h-screen transition-transform -translate-x-full sm:translate-x-0"/>
        <div class="p-4 sm:ml-64">
            <router-view />
        </div>
    </div>
    <div v-else class="layout-container">
        <div v-if="route.path !== '/login' && route.path !== '/sign-up'" class="layout-grid">
            <AppTopbar />
            <router-view /> 
            <AppFooter />
        </div>
        <div v-else>
            <router-view />
        </div>
    </div>
</template>
