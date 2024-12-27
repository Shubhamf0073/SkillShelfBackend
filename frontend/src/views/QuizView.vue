<template>
    <div class="quiz">
      <h1>Course Recommendation Quiz</h1>
      <form @submit.prevent="submitQuiz">
        <div v-for="(question, index) in questions" :key="index">
          <label :for="'question-' + index">{{ question.text }}</label>
          <input type="text" :id="'question-' + index" v-model="answers[index]" required />
        </div>
        <button type="submit">Submit</button>
      </form>
      <div v-if="recommendedCourse">
        <h2>Recommended Course</h2>
        <p>{{ recommendedCourse.course_name }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        questions: [
          { text: "Preferred difficulty level (encoded)?" },
          { text: "Preferred course rating?" },
          { text: "Preferred description word count?" },
          { text: "Preferred about length?" },
          { text: "Preferred course description length?" },
          // Add more questions as needed
        ],
        answers: [],
        recommendedCourse: null,
      };
    },
    methods: {
      async submitQuiz() {
        try {
          const response = await fetch('http://localhost:8000/api/recommend/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ answers: this.answers }),
          });
          const data = await response.json();
          this.recommendedCourse = data.recommended_course;
        } catch (error) {
          console.error('Error submitting quiz:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .quiz {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  form {
    display: flex;
    flex-direction: column;
  }
  label {
    margin-top: 10px;
  }
  button {
    margin-top: 20px;
  }
  </style>