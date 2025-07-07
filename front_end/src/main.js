import "./assets/styles/main.css";

import { createApp } from "vue";
import PrimeVue from "primevue/config";
import ToastService from 'primevue/toastservice';
import App from "./App.vue";
import Aura from "@primeuix/themes/aura";
import { createRouter, createWebHistory } from "vue-router";
import Home from "./views/Home.vue";
import News from "./views/News.vue";
import DetailNews from "./views/DetailNews.vue";
import Login from "./views/Login.vue";
import SignUp from "./views/SignUp.vue";

async function validateTokenWithBackend() {
  const token = localStorage.getItem("token");
  if (!token) return false;
  try {
    const res = await fetch(`${import.meta.env.VITE_API_URL}/validate`, {
      headers: {
      Authorization: `Bearer ${token}`,
      },
    });
    if (!res.ok) return false;
    const data = await res.json();
    return data.valid === true;
  } catch (e) {
    return false;
  }
}

const app = createApp(App);

const routes = [
  { 
    path: "/", 
    component: Home, 
    name: "home", 
    meta: { requiresAuth: true } 
  },
  { 
    path: "/news", 
    component: News, 
    name: "news"
  },
  { 
    path: "/news/:id", 
    component: DetailNews, 
    props: true, 
    name: "detail-news"
  },
  { 
    path: "/login", 
    component: Login, 
    name: "login",
    meta: { guestOnly: true }
  },
  { 
    path: "/sign-up", 
    component: SignUp, 
    name: "sign-up",
    meta: { guestOnly: true }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const token = localStorage.getItem("token");

  if (to.meta.requiresAuth) {
    if (!token) {
      next({ name: "login" });
    } else {
      const valid = await validateTokenWithBackend();
      if (!valid) {
        localStorage.removeItem("token");
        next({ name: "login" });
      } else {
        next();
      }
    }
  } else if (to.meta.guestOnly) {
    if (token) {
      const valid = await validateTokenWithBackend();
      if (valid) {
        next({ name: "home" });
      } else {
        localStorage.removeItem("token");
        next();
      }
    } else {
      next();
    }
  } else {
    next();
  }
});

app.use(PrimeVue, {
  theme: {
    preset: Aura,
    options: {
      darkModeSelector: ".p-dark",
    },
  },
});
app.use(ToastService);
app.use(router);

app.mount("#app");
