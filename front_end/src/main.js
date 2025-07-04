import "./assets/styles/main.css";

import { createApp } from "vue";
import PrimeVue from "primevue/config";
import App from "./App.vue";
import Aura from "@primeuix/themes/aura";
import { createRouter, createWebHistory } from "vue-router";
import Home from "./views/Home.vue";
import News from "./views/News.vue";

const app = createApp(App);

const routes = [
  { path: "/", component: Home },
  { path: "/news", component: News },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

app.use(PrimeVue, {
  theme: {
    preset: Aura,
    options: {
      darkModeSelector: ".p-dark",
    },
  },
});

app.use(router);

app.mount("#app");
