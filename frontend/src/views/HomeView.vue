<template>
  <div class="home">
    <h1>Recommender System</h1>
    <RecommenderComponent />
  </div>
</template>

<script>
import RecommenderComponent from '@/components/RecommenderComponent.vue';

export default {
  name: 'HomeView',
  components: {
    RecommenderComponent,
  },
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>