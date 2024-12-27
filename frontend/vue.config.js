module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/recommender-system-project/' : '/',
  outputDir: '../backend/recommender_system/static',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    },
  },
};