<template>
  <div class="d-flex flex-column mt-4">

    <v-btn
        prepend-icon="mdi-compare-horizontal"
        size="small"
        class="mb-2"
        @click="addToCompare()"
    >
      Добавить к сравнению
    </v-btn>

    <h2 class="text-h4">{{ item.manufacturer }} {{ item.name }}</h2>
    <h5>Год выпуска: {{ item.year }}</h5>

    <v-divider class="my-2"></v-divider>

    <h5 class="text-subtitle-1">Привод: {{ item.transmission }}</h5>
    <h5 class="text-subtitle-1">Л.с.: {{ item.hp }}</h5>
  </div>
</template>

<script>
export default {
  name: "CarItem",
  props: ['car'],
  data() {
    return {
      item: this.car
    }
  },
  methods: {
    addToCompare() {
      const car1 = localStorage.getItem('car1')
      if (car1) {
        localStorage.setItem('car2', this.item.id)
        this.$notify('Добавено к сравнению #2')
      } else {
        localStorage.setItem('car1', this.item.id)
        this.$notify('Добавено к сравнению #1')
      }
    }
  }
}
</script>

<style scoped>

</style>