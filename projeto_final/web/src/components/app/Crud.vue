<template>
  <v-container fill-height
               fluid
               grid-list-md>
    <v-flex sm12>
      <app-crud-form
        ref="form"
        :title="`Editor de ${title}`"
        :api-save="getAction(apiSave)"
        :form="form"
        :form-items="formItems"
        @reload="reload"
        @clearForm="clearForm"
      ></app-crud-form>
      <app-crud-table
        :title="title"
        :headers="headers"
        :loading="loading"
        :data="data"
        :api-remove="getAction(apiRemove)"
        @reloadItems="reload"
        @editItem="edit"
        @selectedRow="selectedRow"
      >
        <template v-slot:extras>
          <slot name="extras"/>
        </template>
      </app-crud-table>
    </v-flex>
  </v-container>
</template>

<script>
export default {
  props: {
    title: {
      type: String
    },
    items: {
      required: true
    },
    data: {
      required: true,
      type: Array
    },
    apiModule: {
      type: String
    },
    apiLoad: {
      type: String,
      default: 'load'
    },
    apiSave: {
      type: String,
      default: 'save'
    },
    apiRemove: {
      type: String,
      default: 'remove'
    }
  },
  data () {
    return {
      loading: false,
      form: {}
    }
  },
  computed: {
    headers () {
      return this.items.filter(f => typeof f.showInTable === 'undefined' ? true : f.showInTable)
    },
    formItems () {
      return this.items.filter(f => f.value !== 'id' && f.value !== '' && f.value.indexOf('display') === -1)
    }
  },
  methods: {
    getAction (action) {
      if (this.apiModule) {
        return `${this.apiModule}/${action}`
      }
      return action
    },
    reload () {
      this.loading = true
      this.$store.dispatch(this.getAction(this.apiLoad))
        .then(() => (this.loading = false))
        .catch(err => {
          this.error.has = true
          this.error.message = err
        })
    },
    edit (item) {
      this.form = item
      this.$refs.form.show()
    },
    clearForm () {
      this.form = {}
    },
    selectedRow (item) {
      this.$emit('selectedRow', item)
    }
  },
  mounted () {
    this.reload()
  }
}
</script>

<style scoped>

</style>
