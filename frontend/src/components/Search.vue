<template>
  <div>
    <div class="d-flex">
      <v-progress-linear
        v-if="dataInProgress"
        indeterminate
        color="pink-accent-3"
      />
    </div>
    <div class="d-flex flex-row">
      <v-select
        v-model="selectedManufacturer"
        :items="manufacturers"
        item-title="name"
        item-value="id"
        label="Производитель"
        variant="solo"
        class="me-1"
      />
      <v-select
        class="ms-1"
        v-model="selectedCar"
        :items="cars[selectedManufacturer]"
        item-title="name"
        item-value="id"
        label="Автомобиль"
        :disabled="!selectedManufacturer"
        variant="solo"
      />
    </div>
    <div class="d-flex">
      <v-btn style="flex: auto" color="blue-darken-1" :disabled="!selectedCar" @click="doSearch">
        <v-icon icon="mdi-magnify"></v-icon>
        Показать
      </v-btn>
    </div>
    <div class="d-flex mt-3" v-if="carItem && dataReceived">
      <CarItem v-bind:car="carItem" />
    </div>
    <div class="d-flex mt-3" style="flex-flow: column" v-if="carItem && dataReceived">
      <Comments v-bind:car="carItem" />
    </div>
  </div>
</template>

<script>
import CarItem from "./CarItem.vue";
import Comments from "./Comments.vue";
export default {
  name: "Search",
  components: {Comments, CarItem},
  data() {
    return {
      selectedManufacturer: null,
      selectedCar: null,
      dataInProgress: false,
      dataReceived: false,
      carItem: null,
      manufacturers: [
        {
          name: 'Toyota',
          id: 1
        }, {
          name: 'Honda',
          id: 2
        }
      ],
      cars: {
        '1': [
          {
            name: 'Corolla',
            year: '2020'
          }, {
            name: 'Land Cruiser',
            year: '2019'
          }
        ],
        '2': [
          {
            name: 'Civic',
            year: '2021'
          }, {
            name: 'Inspire',
            year: '2019'
          }
        ]
      }
    }
  },
  watch: {
    selectedManufacturer() {
      this.selectedCar = null
    }
  },
  methods: {
    doSearch() {
      this.carItem = null
      this.dataReceived = false
      this.dataInProgress = true
      setTimeout(() => {
        this.dataInProgress = false
        this.dataReceived = true
        this.carItem = {
          manufacturer: 'Toyota',
          name: 'Corolla',
          id: 3,
          year: 2020,
          hp: 122,
          transmission: 'fwd'
        }
        this.$notify('Данные получены')
        this.$notify({
          type: 'error',
          text: 'Ошибка'
        })
      }, 150)
    }
  }
}
</script>

<style scoped>

</style>