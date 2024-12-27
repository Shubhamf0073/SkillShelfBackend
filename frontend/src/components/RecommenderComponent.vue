<template>
  <div class="recommender">
    <h1>Recommender System</h1>
    <div>
      <label for="input">Enter your preferences:</label>
      <input type="text" v-model="userInput" id="input" />
      <button @click="getRecommendations">Get Recommendations</button>
    </div>
    <div v-if="recommendations.length">
      <h2>Recommendations:</h2>
      <ul>
        <li v-for="(item, index) in recommendations" :key="index">{{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: '',
      recommendations: []
    };
  },
  methods: {
    async getRecommendations() {
      try {
        const response = await fetch(`http://localhost:8000/api/recommend?input=${this.userInput}`);
        const data = await response.json();
        this.recommendations = data.recommendations;
      } catch (error) {
        console.error('Error fetching recommendations:', error);
      }
    }
  }
};
</script>

<style scoped>
.recommender {
  padding: 20px;
}
</style>