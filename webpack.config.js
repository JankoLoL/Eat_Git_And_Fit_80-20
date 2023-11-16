const path = require("path");
const webpack = require("webpack");


module.exports = {
  mode: "none",
  entry: `./eat_fit_app/static/src/main.jsx`,
  devtool: "inline-source-map",
  output: {
    filename: "main.js",
    path: path.join(__dirname, `./eat_fit_app/static/js/`),
    clean: false,

  },
  // devServer: {
  //   open: true,
  //   hot: true,
  //   static: [
  //     {
  //       directory: path.join(__dirname, entryPath),
  //       publicPath: "/",
  //       serveIndex: true,
  //     },
  //   ],
  //   devMiddleware: {
  //     writeToDisk: true,
  //   },
  //   compress: true,
  //   port: 3001,
  //   historyApiFallback: true,
  // },
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
    ],
  },
  plugins: [
    new webpack.ProvidePlugin({
      process: "process/browser",
    }),
  ],
};
