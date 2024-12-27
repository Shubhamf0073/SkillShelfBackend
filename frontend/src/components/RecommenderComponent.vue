<template>
  <div>
    <h2>Recommended Courses</h2>
    <ul>
      <li v-for="course in courses" :key="course.id">{{ course.course_name }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      courses: [],
    };
  },
  created() {
    this.fetchCourses();
  },
  methods: {
    async fetchCourses() {
      try {
        const response = await fetch('http://localhost:8000/api/courses/');
        this.courses = await response.json();
      } catch (error) {
        console.error('Error fetching courses:', error);
      }
    },
  },
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 5px 0;
}
</style>