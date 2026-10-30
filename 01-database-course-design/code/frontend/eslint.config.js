import globals from 'globals';
import pluginVue from 'eslint-plugin-vue';
import standard from '@vue/eslint-config-standard';

// ESLint v9 flat configuration
export default [
  {
    languageOptions: {
      globals: {
        ...globals.node,
        ...globals.browser
      }
    }
  },
  {
    files: ['**/*.vue', '**/*.js']
  },
  ...pluginVue.configs['flat/essential'],
  {
    rules: {
      'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
      'vue/multi-word-component-names': 'off',
      'semi': ['error', 'always'],
      'quotes': ['error', 'single']
    }
  }
];
