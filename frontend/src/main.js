import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'vuetify/styles'
import { createVuetify } from "vuetify"
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import Notifications from '@kyvg/vue3-notification'

import "@mdi/font/css/materialdesignicons.css"

const app = createApp(App)
const vuetify = createVuetify({
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi
    }
  },
  components,
  directives
})

app.use(router)
app.use(vuetify)
app.use(Notifications)

app.mount('#app')
