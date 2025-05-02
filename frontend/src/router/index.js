import {createRouter, createWebHistory} from 'vue-router'

import HomePage from '@/views/HomePage.vue'
import InfoCardsPage from '@/views/InfoCardsPage.vue'
import RawStockPage from '@/views/RawStockPage.vue'
import FinishedStockPage from '@/views/FinishedStockPage.vue'
import ProductionPlanPage from '@/views/ProductionPlanPage.vue'
import LineStatusPage from '@/views/LineStatusPage.vue'
import UsersPage from '@/views/UsersPage.vue'
import LoginPage from '@/views/LoginPage.vue'

// Новые страницы справочников
import InfoCard from '@/views/info/InfoCard.vue'
import LinesInfo from '@/views/info/LinesInfo.vue'
import FinishedProductsInfo from '@/views/info/FinishedProductsInfo.vue'
import MaintenanceInfo from '@/views/info/MaintenanceInfo.vue'
import Onboarding from '@/views/info/Onboarding.vue'
import RawMaterialsInfo from '@/views/info/RawMaterialsInfo.vue'
import StandardsInfo from '@/views/info/StandardsInfo.vue'
import TechnologicalInfo from '@/views/info/TechnologicalInfo.vue'

const isAdmin = () => {
  // Тут твоя реальная проверка
  // Например, проверка по localStorage
  // return localStorage.getItem('role') === 'admin'
  return true
}

const routes = [
  {path: '/', component: HomePage},
  {path: '/info-cards', component: InfoCardsPage},
  {path: '/info-cards/production-lines', component: LinesInfo},
  {path: '/info-cards/technological-cards', component: TechnologicalInfo},
  {path: '/info-cards/finished-products', component: FinishedProductsInfo},
  {path: '/info-cards/raw-materials', component: RawMaterialsInfo},
  {path: '/info-cards/maintenance', component: MaintenanceInfo},
  {path: '/info-cards/onboarding', component: Onboarding},
  {path: '/info-cards/standards', component: StandardsInfo},
  {path: '/raw-stock', component: RawStockPage},
  {path: '/finished-stock', component: FinishedStockPage},
  {path: '/production-plan', component: ProductionPlanPage},
  {path: '/line-status', component: LineStatusPage},
  {
    path: '/users',
    component: UsersPage,
    beforeEnter: (to, from, next) => {
      if (isAdmin()) {
        next()
      } else {
        next('/') // Редирект на главную, если не админ
      }
    }
  },
  {path: '/info-card/:id', name: 'info-card', component: InfoCard, props: true},
  {path: '/login', component: LoginPage}
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
