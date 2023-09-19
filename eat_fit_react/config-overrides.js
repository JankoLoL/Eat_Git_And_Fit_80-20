const BundleTracker = require("webpack-bundle-tracker");

module.exports = function override(config, env) {
  if (!config.plugins) {
    config.plugins = [];
  }

  config.plugins.push(new BundleTracker({ filename: './webpack-stats.json' }));

  return config;
};
