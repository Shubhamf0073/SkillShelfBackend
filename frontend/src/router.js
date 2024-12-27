import Vue from 'vue';
import Router from 'vue-router';
import HomeView from './views/HomeView.vue';
import RecommenderComponent from './components/RecommenderComponent.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/recommender',
      name: 'recommender',
      component: RecommenderComponent
    }
  ]
});