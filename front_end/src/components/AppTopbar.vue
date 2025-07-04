<script setup>
import { useLayout } from "../composables/useLayout";
import AppConfig from "./AppConfig.vue";
import { useRouter, useRoute } from "vue-router";
import { ref } from "vue";

const router = useRouter();
const route = useRoute();
const token = localStorage.getItem("token");

const { isDarkMode, toggleDarkMode } = useLayout();

const items = ref([
  {
    label: "Home",
    icon: "pi pi-home",
    route: "/",
  },
  {
    label: "News",
    icon: "pi pi-book",
    route: "/news",
  },
  {
    label: "About",
    icon: "pi pi-info-circle",
    route: "/about",
  },
]);

function logout() {
  localStorage.removeItem("token");
  router.push({ name: "login" });
}

const showMobileMenu = ref(false);
function toggleMobileMenu() {
  showMobileMenu.value = !showMobileMenu.value;
}
</script>

<template>
  <div class="topbar">
    <div class="topbar-container">
      <div class="topbar-brand">
        <svg
          width="35"
          height="40"
          viewBox="0 0 35 40"
          fill="none"
          class="w-8"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M25.87 18.05L23.16 17.45L25.27 20.46V29.78L32.49 23.76V13.53L29.18 14.73L25.87 18.04V18.05ZM25.27 35.49L29.18 31.58V27.67L25.27 30.98V35.49ZM20.16 17.14H20.03H20.17H20.16ZM30.1 5.19L34.89 4.81L33.08 12.33L24.1 15.67L30.08 5.2L30.1 5.19ZM5.72 14.74L2.41 13.54V23.77L9.63 29.79V20.47L11.74 17.46L9.03 18.06L5.72 14.75V14.74ZM9.63 30.98L5.72 27.67V31.58L9.63 35.49V30.98ZM4.8 5.2L10.78 15.67L1.81 12.33L0 4.81L4.79 5.19L4.8 5.2ZM24.37 21.05V34.59L22.56 37.29L20.46 39.4H14.44L12.34 37.29L10.53 34.59V21.05L12.42 18.23L17.45 26.8L22.48 18.23L24.37 21.05ZM22.85 0L22.57 0.69L17.45 13.08L12.33 0.69L12.05 0H22.85Z"
            class="fill-primary"
          />
          <path
            d="M30.69 4.21L24.37 4.81L22.57 0.69L22.86 0H26.48L30.69 4.21ZM23.75 5.67L22.66 3.08L18.05 14.24V17.14H19.7H20.03H20.16H20.2L24.1 15.7L30.11 5.19L23.75 5.67ZM4.21002 4.21L10.53 4.81L12.33 0.69L12.05 0H8.43002L4.22002 4.21H4.21002ZM21.9 17.4L20.6 18.2H14.3L13 17.4L12.4 18.2L12.42 18.23L17.45 26.8L22.48 18.23L22.5 18.2L21.9 17.4ZM4.79002 5.19L10.8 15.7L14.7 17.14H14.74H15.2H16.85V14.24L12.24 3.09L11.15 5.68L4.79002 5.2V5.19Z"
            class="fill-surface"
          />
        </svg>
        <span class="topbar-brand-text">
          <span class="topbar-title">News</span>
          <span class="topbar-subtitle">Update</span>
        </span>
      </div>
      <button class="topbar-hamburger" @click="toggleMobileMenu">
        <i class="pi pi-bars"></i>
      </button>
      <div class="topbar-menu-horizontal">
        <ul class="topbar-menu-list-horizontal">
          <li
            v-for="item in items"
            :key="item.label"
            class="topbar-menu-item-horizontal"
          >
            <router-link
              v-if="item.route"
              :to="item.route"
              class="topbar-menu-link"
              :class="{ active: route.path === item.route }"
            >
              <Button
                :label="item.label"
                :icon="item.icon"
                text
                rounded
              />
            </router-link>
            <Button
              v-else
              :label="item.label"
              :icon="item.icon"
              text
              rounded
              @click="item.command && item.command()"
            />
          </li>
        </ul>
      </div>
      <transition name="fade">
        <div class="topbar-menu-mobile" v-if="showMobileMenu">
          <ul>
            <li v-for="item in items" :key="item.label">
              <router-link
                v-if="item.route"
                :to="item.route"
                class="topbar-menu-link"
                :class="{ active: route.path === item.route }"
                @click="showMobileMenu = false"
              >
                <Button :label="item.label" :icon="item.icon" text rounded />
              </router-link>
              <Button
                v-else
                :label="item.label"
                :icon="item.icon"
                text
                rounded
                @click="item.command && item.command()"
              />
            </li>
          </ul>
        </div>
      </transition>
      <div class="topbar-actions">
        <Button
          type="button"
          class="topbar-theme-button"
          @click="toggleDarkMode"
          text
          rounded
        >
          <i
            :class="[
              'pi ',
              'pi ',
              { 'pi-moon': isDarkMode, 'pi-sun': !isDarkMode },
            ]"
          />
        </Button>
        <div class="relative">
          <Button
            v-styleclass="{
              selector: '@next',
              enterFromClass: 'hidden',
              enterActiveClass: 'animate-scalein',
              leaveToClass: 'hidden',
              leaveActiveClass: 'animate-fadeout',
              hideOnOutsideClick: true,
            }"
            icon="pi pi-cog"
            text
            rounded
            aria-label="Settings"
          />
          <AppConfig />
        </div>
        <div class="relative">
            <Button
            v-if="token"
            icon="pi pi-sign-out"
            text
            rounded
            @click="logout()"
            />
            <router-link
            v-else
            :to="{ name: 'login' }"
            >
            <Button
              icon="pi pi-sign-in"
              text
              rounded
            />
            </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.topbar-menu-link.active .p-button {
  background-color: var(--p-primary-50);
  color: var(--p-primary-500);
  font-weight: bold;
}
.topbar-hamburger {
  color: var(--p-primary-500);
  display: none;
  background: none;
  border: none;
  font-size: 2rem;
  margin-left: 1rem;
  cursor: pointer;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .topbar-container {
    flex-wrap: wrap;
    padding: 0.5rem 1rem;
  }
  .topbar-menu-horizontal {
    display: none;
  }
  .topbar-hamburger {
    display: block;
  }
  .topbar-menu-mobile {
    display: block;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: var(--surface-0, #fff);
    box-shadow: 0 4px 24px 0 rgba(0,0,0,0.08);
    z-index: 1000;
    position: absolute;
    padding: 1rem 0;
  }
  .topbar-menu-mobile ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .topbar-menu-mobile li {
    margin: 0.5rem 1.5rem;
  }
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>