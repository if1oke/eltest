<script setup>
import Main from "./components/Main.vue";
localStorage.clear()
</script>

<template>
  <header>

    <notifications position="bottom right"/>
    <div class="wrapper">
      <Main />
    </div>

  </header>
</template>

<style scoped>

</style>
