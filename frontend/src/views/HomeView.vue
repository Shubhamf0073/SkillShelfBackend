<template>
  <div class="home">
    <h1>Welcome to the Recommender System</h1>
    <p>Explore our recommendations based on your preferences!</p>
    <RecommenderComponent />
  </div>
</template>

<script>
import RecommenderComponent from '../components/RecommenderComponent.vue';

export default {
  name: 'HomeView',
  components: {
    RecommenderComponent
  }
};
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 50px;
}
</style>