<template>
  <v-container fluid>

    <!-- Заголовок текущей смены -->
    <h1 class="page-title">Текущая смена:
      <v-chip class="pl-6 pr-6" color="green" variant="flat" size="x-large">
        <h2>C</h2>
      </v-chip>
    </h1>

    <v-row no-gutters align="stretch" justify="space-between">
      <!-- Статус производственных линий -->
      <v-col>
        <v-card class="pa-2 ma-2" min-height="230">
          <h3>Статус производственных линий</h3>
          <ProductionLinesStatus/>
        </v-card>
      </v-col>
      <!-- Текущая продукция в производстве -->
      <v-col>
        <v-card class="pa-2 ma-2" min-height="230">
          <h3>Текущая продукция в производстве</h3>
          <CurrentProducts/>
        </v-card>
      </v-col>
    </v-row>

    <v-row justify="center">
      <!-- Выполнение плана производства -->
      <v-col cols="12">
        <v-card class="pa-2">
          <h3 class="mb-2">Выполнение плана производства</h3>
          <ProductionPlanProgress/>
        </v-card>
      </v-col>
    </v-row>

    <v-row justify="center">
      <!-- Важные уведомления -->
      <v-col cols="12">
        <v-card class="pa-2">
          <h3>Важные уведомления</h3>
          <ImportantNotifications/>
        </v-card>
      </v-col>
    </v-row>

  </v-container>
</template>

<script setup>
import ProductionLinesStatus from "@/components/ProductionLinesStatus.vue";
import CurrentProducts from "@/components/CurrentProducts.vue";
import ProductionPlanProgress from "@/components/ProductionPlanProgress.vue";
import ImportantNotifications from "@/components/ImportantNotifications.vue";
</script>

<style scoped>
.page-title {
  font-size: 28px;
  margin-bottom: 1.5rem;
}
</style>
