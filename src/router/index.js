import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/views/Home.vue';
import Customization from '@/views/Customization.vue';
import Scan from '@/views/Scan.vue';
import Public from '@/views/Public.vue';
import Explore from '@/views/Explore.vue';
import SignUp from '@/views/SignUp.vue';   // <-- add this
import Subscribe from '@/views/Subscribe.vue'; // <-- add this if you want plans

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/customize', name: 'Customization', component: Customization },
    { path: '/scan', name: 'Scan', component: Scan },
    { path: '/public', name: 'Public', component: Public },
    { path: '/explore', name: 'Explore', component: Explore },
    { path: '/signup', name: 'SignUp', component: SignUp },       // ✅ now wired
    { path: '/subscribe', name: 'Subscribe', component: Subscribe } // optional
  ]
});

