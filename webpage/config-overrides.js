/* tslint:disable */

module.exports = function override(config, env) {
  // Less support
  config.module.rules[1].oneOf.unshift(
    {
      test: /\.less$/,
      exclude: /antd\.less|node_modules/,
      use: [
        require.resolve('style-loader'),
        {
          loader: require.resolve('css-loader'),
          options: {
            importLoaders: 1,
            minimize: true,
            modules: true,
            localIdentName: '[local]___[hash:base64:5]'
          }
        },
        {
          loader: require.resolve('postcss-loader'),
          options: {
            ident: 'postcss',
            plugins: () => []
          }
        },
        {
          loader: require.resolve('less-loader')
        }
      ]
    }
  );

  return config;
};