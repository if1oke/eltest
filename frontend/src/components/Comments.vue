<template>
  <div>
    <v-card v-for="item in items" class="my-1">
      <v-card-text class="pb-1">
        <p>{{ item.comment }}</p>
        <h6 style="color: gray">{{ item.created_at }}</h6>
      </v-card-text>
    </v-card>
    <v-card-text class="pb-0">
      <v-text-field
        density="compact"
        v-model="comment"
        variant="solo"
        label="Оставить комментарий"
        append-inner-icon="mdi-send-circle"
        hide-details="auto"
        @click:append-inner="sendComment"
      ></v-text-field>
    </v-card-text>
  </div>
</template>


<script>
import moment from "moment";

export default {
  name: "Comments",
  data() {
    return {
      comment: null,
      items: [
        {id: 1, comment: 'Hell world', created_at: '2023-03-01 22:15:01'},
        {id: 1, comment: 'Hell1231 world', created_at: '2023-03-01 22:15:01'}
      ]
    }
  },
  methods: {
    sendComment() {
      this.items.push(
          {id: 1, comment: this.comment, created_at: moment().format('YYYY-MM-DD HH:mm:ss')}
      )
    }
  }
}
</script>

<style scoped>

</style>