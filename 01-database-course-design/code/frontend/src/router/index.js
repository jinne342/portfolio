import { createRouter, createWebHistory } from 'vue-router';
import { useUserStore } from '../store/user.js';

// 页面组件
import Home from '../views/Home.vue';
import NewHome from '../views/NewHome.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Dashboard from '../views/Dashboard.vue';
import CompetitionDetail from '../views/CompetitionDetail.vue';
import CompetitionNews from '../views/CompetitionNews.vue';
import OrganizationStructure from '../views/OrganizationStructure.vue';
import CompetitionTime from '../views/CompetitionTime.vue';
import AwardQuery from '../views/AwardQuery.vue';
import ApplyCooperation from '../views/ApplyCooperation.vue';
import PastReviews from '../views/PastReviews.vue';
import Feedback from '../views/Feedback.vue';

// 学生页面
import StudentDashboard from '../views/student/StudentDashboard.vue';
import StudentTeam from '../views/student/StudentTeam.vue';
import StudentSubmission from '../views/student/StudentSubmission.vue';
import StudentCertificate from '../views/student/StudentCertificate.vue';
import StudentMessage from '../views/student/StudentMessage.vue';
import StudentCompetition from '../views/student/StudentCompetition.vue';
import StudentProblem from '../views/student/StudentProblem.vue';

// 教师页面
import TeacherDashboard from '../views/teacher/TeacherDashboard.vue';
import TeacherTeam from '../views/teacher/TeacherTeam.vue';
import TeacherReview from '../views/teacher/TeacherReview.vue';
import TeacherStatistics from '../views/teacher/TeacherStatistics.vue';
import TeacherMessage from '../views/teacher/TeacherMessage.vue'; // 新添加

// 管理员页面
import AdminDashboard from '../views/admin/AdminDashboard.vue';
import AdminUser from '../views/admin/AdminUser.vue';
import AdminTeam from '../views/admin/AdminTeam.vue';
import AdminCompetition from '../views/admin/AdminCompetition.vue';
import AdminViolation from '../views/admin/AdminViolation.vue';
import AdminStatistics from '../views/admin/AdminStatistics.vue';
import AdminMessage from '../views/admin/AdminMessage.vue'; // 新添加
import AdminRegistrationAudit from '../views/admin/AdminRegistrationAudit.vue'; // 报名审核页面

// 评审页面
import ReviewerDashboard from '../views/reviewer/ReviewerDashboard.vue';
import ReviewerReview from '../views/reviewer/ReviewerReview.vue';
import ReviewerMessage from '../views/reviewer/ReviewerMessage.vue'; // 新添加

// 通用页面
import University from '../views/University.vue';
import College from '../views/College.vue';
import Team from '../views/Team.vue';
import TeamDetail from '../views/TeamDetail.vue';
import Problem from '../views/Problem.vue';
import Submission from '../views/Submission.vue';
import Review from '../views/Review.vue';
import Message from '../views/Message.vue';
import Announcement from '../views/Announcement.vue';
import Violation from '../views/Violation.vue';
import Certificate from '../views/Certificate.vue';
import Statistics from '../views/Statistics.vue';
import Archive from '../views/Archive.vue';

const routes = [
  { path: '/', component: NewHome, meta: { requiresAuth: false } },
  { path: '/login', component: Login, meta: { requiresAuth: false } },
  { path: '/register', component: Register, meta: { requiresAuth: false } },
  
  // 新增页面路由
  { path: '/competition-detail', component: CompetitionDetail, meta: { requiresAuth: false } },
  { path: '/competition-news', component: CompetitionNews, meta: { requiresAuth: false } },
  { path: '/organization-structure', component: OrganizationStructure, meta: { requiresAuth: false } },
  { path: '/competition-time', component: CompetitionTime, meta: { requiresAuth: false } },
  { path: '/award-query', component: AwardQuery, meta: { requiresAuth: false } },
  { path: '/apply-cooperation', component: ApplyCooperation, meta: { requiresAuth: false } },
  { path: '/past-reviews', component: PastReviews, meta: { requiresAuth: false } },
  { path: '/feedback', component: Feedback, meta: { requiresAuth: false } },
  
  // 学生路由
  { path: '/student/dashboard', component: StudentDashboard, meta: { requiresAuth: true, role: ['学生'] } },
  { path: '/student/team', component: StudentTeam, meta: { requiresAuth: true, role: ['学生'] } },
  { path: '/student/submission', component: StudentSubmission, meta: { requiresAuth: true, role: ['学生'] } },
  { path: '/student/certificate', component: StudentCertificate, meta: { requiresAuth: true, role: ['学生'] } },
  { path: '/student/message', component: StudentMessage, meta: { requiresAuth: true, role: ['学生'] } },
  { path: '/student/competition', component: StudentCompetition, meta: { requiresAuth: true, role: ['学生'] } },
  { path: '/student/problem', component: StudentProblem, meta: { requiresAuth: true, role: ['学生'] } },
  
  // 教师路由
  { path: '/teacher/dashboard', component: TeacherDashboard, meta: { requiresAuth: true, role: ['教师'] } },
  { path: '/teacher/team', component: TeacherTeam, meta: { requiresAuth: true, role: ['教师'] } },
  { path: '/teacher/review', component: TeacherReview, meta: { requiresAuth: true, role: ['教师'] } },
  { path: '/teacher/statistics', component: TeacherStatistics, meta: { requiresAuth: true, role: ['教师'] } },
  { path: '/teacher/message', component: TeacherMessage, meta: { requiresAuth: true, role: ['教师'] } }, // 新添加
  
  // 竞赛管理员路由
  { path: '/competition-admin/dashboard', component: AdminDashboard, meta: { requiresAuth: true, role: ['竞赛管理员'] } },
  { path: '/competition-admin/team', component: AdminTeam, meta: { requiresAuth: true, role: ['竞赛管理员'] } },
  { path: '/competition-admin/competition', component: AdminCompetition, meta: { requiresAuth: true, role: ['竞赛管理员'] } },
  { path: '/competition-admin/registration-audit', component: AdminRegistrationAudit, meta: { requiresAuth: true, role: ['竞赛管理员'] } },
  { path: '/competition-admin/message', component: AdminMessage, meta: { requiresAuth: true, role: ['竞赛管理员'] } },
  
  // 超级管理员路由
  { path: '/super-admin/dashboard', component: AdminDashboard, meta: { requiresAuth: true, role: ['超级管理员'] } },
  { path: '/super-admin/user', component: AdminUser, meta: { requiresAuth: true, role: ['超级管理员'] } },
  { path: '/super-admin/team', component: AdminTeam, meta: { requiresAuth: true, role: ['超级管理员'] } },
  { path: '/super-admin/competition', component: AdminCompetition, meta: { requiresAuth: true, role: ['超级管理员'] } },
  { path: '/super-admin/violation', component: AdminViolation, meta: { requiresAuth: true, role: ['超级管理员'] } },
  { path: '/super-admin/statistics', component: AdminStatistics, meta: { requiresAuth: true, role: ['超级管理员'] } },
  { path: '/super-admin/message', component: AdminMessage, meta: { requiresAuth: true, role: ['超级管理员'] } },
  
  // 评审路由已合并到教师角色
  { path: '/reviewer/dashboard', component: TeacherDashboard, meta: { requiresAuth: true, role: ['教师'] } },
  { path: '/reviewer/review', component: TeacherReview, meta: { requiresAuth: true, role: ['教师'] } },
  { path: '/reviewer/message', component: TeacherMessage, meta: { requiresAuth: true, role: ['教师'] } },

  // 通用路由（兼容旧路由）
  { path: '/dashboard', component: Dashboard, meta: { requiresAuth: true } },
  { path: '/university', component: University, meta: { requiresAuth: true } },
  { path: '/college', component: College, meta: { requiresAuth: true } },
  { path: '/team', component: Team, meta: { requiresAuth: true } },
  { path: '/team/:id', component: TeamDetail, props: true, meta: { requiresAuth: true } },
  { path: '/problem', component: Problem, meta: { requiresAuth: true } },
  { path: '/submission', component: Submission, meta: { requiresAuth: true } },
  { path: '/review', component: Review, meta: { requiresAuth: true } },
  { path: '/message', component: Message, meta: { requiresAuth: true } },
  { path: '/announcement', component: Announcement, meta: { requiresAuth: true } },
  { path: '/violation', component: Violation, meta: { requiresAuth: true } },
  { path: '/certificate', component: Certificate, meta: { requiresAuth: true } },
  { path: '/statistics', component: Statistics, meta: { requiresAuth: true } },
  { path: '/archive', component: Archive, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// 路由守卫
router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  
  // 初始化用户信息
  if (!userStore.userInfo.token) {
    userStore.initUser();
  }
  
  // 如果路由需要认证
  if (to.meta.requiresAuth) {
    // 检查是否登录
    if (!userStore.userInfo.token) {
      next('/login');
      return;
    }
    
    // 检查角色权限
    if (to.meta.role) {
      const hasPermission = to.meta.role.some(role => 
        userStore.hasRole(role) || 
        (role === '学生' && userStore.isStudent) ||
        (role === '教师' && userStore.isTeacher) ||
        (role === '竞赛管理员' && userStore.isCompetitionAdmin) ||
        (role === '超级管理员' && userStore.isSuperAdmin) ||
        (role === '管理员' && userStore.isSuperAdmin)
      );
      
      if (!hasPermission) {
        // 根据用户角色跳转到对应的首页
        if (userStore.isStudent) {
          next('/student/dashboard');
        } else if (userStore.isTeacher) {
          next('/teacher/dashboard');
        } else if (userStore.isCompetitionAdmin) {
          next('/competition-admin/dashboard');
        } else if (userStore.isSuperAdmin) {
          next('/super-admin/dashboard');
        } else {
          next('/login');
        }
        return;
      }
    }
  }
  
  // 如果已登录，访问登录页则跳转到对应角色的首页
  if (to.path === '/login' && userStore.userInfo.token) {
    if (userStore.isStudent) {
      next('/student/dashboard');
    } else if (userStore.isTeacher) {
      next('/teacher/dashboard');
    } else if (userStore.isCompetitionAdmin) {
      next('/competition-admin/dashboard');
    } else if (userStore.isSuperAdmin) {
      next('/super-admin/dashboard');
    } else {
      next('/dashboard');
    }
    return;
  }
  
  next();
});

export default router;
