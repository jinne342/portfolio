<template>
  <div class="page-banner" :style="{ backgroundImage: 'url(' + img + ')' }">
    <h1>{{ title }}</h1>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({
  title: String,
  img: String
});
</script>

<style scoped>
.page-banner {
  height: 200px;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 32px;
  font-weight: bold;
  text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
}
</style>
