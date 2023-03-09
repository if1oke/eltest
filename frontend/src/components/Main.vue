<template>
  <v-card flat>
    <v-toolbar
      color="blue-darken-1"
      dark
      extended
      flat
    >

    </v-toolbar>

    <v-card
      class="mx-auto mb-2"
      max-width="700"
      style="margin-top: -64px"
    >
      <v-toolbar flat>
        <v-toolbar-title>
          {{ title }}
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <RouterLink to="/" style="text-decoration: none" class="mx-1">
          <v-btn :class="route === 'home' ? 'v-btn--active' : ''" icon>
            <v-icon icon="mdi-car-search" size="large" :color="route === 'home' ? 'blue-darken-1' : 'grey-darken-4'" />
          </v-btn>
        </RouterLink>

        <RouterLink to="/compare" style="text-decoration: none" class="mx-1">
          <v-btn :class="route === 'compare' ? 'v-btn--active' : ''" icon>
            <v-icon icon="mdi-compare-horizontal" size="large" :color="route === 'compare' ? 'blue-darken-1' : 'grey-darken-4'" />
          </v-btn>
        </RouterLink>

      </v-toolbar>

      <v-divider></v-divider>

      <v-card-text>
        <router-view></router-view>
      </v-card-text>

    </v-card>
  </v-card>
</template>

<script>
import Search from "./Search.vue";
export default {
  name: "Main",
  components: {Search},
  computed: {
    route() {
      if (this.$route.path === '/') return 'home'
      if (this.$route.path === '/compare') return 'compare'
      if (this.$route.path === '/show') return 'show'
      return 'home'
    },
    title() {
      if (this.$route.path === '/') return 'Поиск автомобиля'
      if (this.$route.path === '/compare') return 'Сравнение автомобилей'
      if (this.$route.path === '/show') return 'Просмотр автомобиля'
      return 'home'
    }
  }
}
</script>

<style scoped>

</style>