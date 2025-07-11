<script setup>
import { ref } from "vue";
import { useToast } from "primevue/usetoast";

const toast = useToast();
let username = ref("");
let password = ref("");
let passwordConfirm = ref("");
let email = ref("");
async function signup() {
  try {
    if (password.value !== passwordConfirm.value) {
      showError("Sign Up failed", "Passwords do not match");
      return;
    }
    const response = await fetch(`${import.meta.env.VITE_API_URL}/sign-up`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value,
      }),
    });
    if (!response.ok) {
      showError(
        "Sign Up failed",
        "An unexpected error occurred. Please try again later."
      );
    } else {
      const data = await response.json();
      username.value = "";
        password.value = "";
        passwordConfirm.value = "";
        email.value = "";
      showSuccess(
        "Sign Up successful",
        "You can now log in with your credentials."
      );
    }
  } catch (error) {
    console.log("Sign Up function error:", error);
  }
}
const showError = (message, detail_message) => {
  toast.add({
    severity: "error",
    summary: message,
    detail: detail_message,
    life: 3000,
  });
};
const showSuccess = (message, detail_message) => {
  toast.add({
    severity: "success",
    summary: message,
    detail: detail_message,
    life: 3000,
  });
};
</script>
<template>
  <div class="layout-grid login-panel">
    <Panel>
      <svg
        width="70"
        height="80"
        viewBox="0 0 35 40"
        fill="none"
        class="w-8"
        xmlns="http://www.w3.org/2000/svg"
        style="margin-left: 20%; margin-right: 20%; width: 60%"
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
      <h3
        style="
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
        "
      >
        Sign Up
      </h3>
      <InputGroup style="margin-bottom: 1rem">
        <InputGroupAddon>
          <i class="pi pi-user"></i>
        </InputGroupAddon>
        <InputText v-model="username" placeholder="Username" />
      </InputGroup>
      <InputGroup style="margin-bottom: 1rem">
        <InputGroupAddon>
          <i class="pi pi-envelope"></i>
        </InputGroupAddon>
        <InputText v-model="email" placeholder="Email" />
      </InputGroup>
      <InputGroup style="margin-bottom: 1rem">
        <InputGroupAddon>
          <i class="pi pi-lock"></i>
        </InputGroupAddon>
        <Password v-model="password" toggleMask placeholder="Password" />
      </InputGroup>
      <InputGroup style="margin-bottom: 1rem">
        <InputGroupAddon>
          <i class="pi pi-lock"></i>
        </InputGroupAddon>
        <Password
          v-model="passwordConfirm"
          toggleMask
          placeholder="Password Confirm"
        />
      </InputGroup>
      <Button @click="signup()" label="Sign Up" class="button-center" />
      <router-link :to="{ name: 'login' }" class="text-center">
        Already have an account?
        </router-link>
    </Panel>
  </div>
</template>

<style scoped>
.login-panel {
  max-width: 500px;
  padding-top: 10rem;
}
.text-center {
  text-align: center;
  display: block;
  margin-top: 1rem;
  color: var(--primary-color);
}
</style>
