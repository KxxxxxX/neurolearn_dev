<template>
  <el-row class="top-bar">
    <div class="top-wrapper">
      <div class="user-area pull-right">
        <div class="user-avatar">
          <span class="avatar-img" :style="{ backgroundImage: 'url(' + avatar_url + ')' }"></span>
          <div class="avatar-drop-menu">
            <ul>
              <li @click="goToProfile"><i class="iconfont">&#xe603;</i>Raniac</li>
              <li @click="signOut"><i class="iconfont">&#xe602;</i>Logout</li>
            </ul>
          </div>
        </div>
      </div>
      <el-col :span="8" class="search-area pull-right">
        <el-form>
          <el-form-item>
            <i class="el-icon-search"></i>
            <el-input v-model="search" placeholder="Search"></el-input>
          </el-form-item>
        </el-form>
      </el-col>
      <div class="new-message-area pull-right">
        <div class="new-message-icon">
          <el-badge class="new-message-badge" is-dot>
            <el-button class="new-message-button" @click="goToAnalysis" size="small" type="primary" icon="el-icon-message" circle></el-button>
          </el-badge>
          <div class="new-message-drop-menu">
            <ul>
              <li>Task 20190404161616 finished!</li>
              <li>Task 20190226121339 failed!</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </el-row>
</template>

<script>
export default {
  data () {
    return {
      avatar_url: 'https://avatars2.githubusercontent.com/u/17725948?s=460&v=4',
      search: ''
    }
  },
  methods: {
    goToProfile () {
      this.$router.replace({
        path: '/profile',
        component: resolve => require(['@/pages/profile'], resolve)
      })
    },
    goToAnalysis () {
      this.$router.replace({
        path: '/analysis/overview',
        component: resolve => require(['@/pages/analysis/overview'], resolve)
      })
    },
    signOut () {
      console.log('Signed out.')
    }
  }
}
</script>

<style lang="scss">
@font-face {
  font-family: 'iconfont';
  src: url('//at.alicdn.com/t/font_1476180127_2466838.eot'); /* IE9*/
  src: url('//at.alicdn.com/t/font_1476180127_2466838.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
  url('//at.alicdn.com/t/font_1476180127_2466838.woff') format('woff'), /* chrome、firefox */
  url('//at.alicdn.com/t/font_1476180127_2466838.ttf') format('truetype'), /* chrome、firefox、opera、Safari, Android, iOS 4.2+*/
  url('//at.alicdn.com/t/font_1476180127_2466838.svg#iconfont') format('svg'); /* iOS 4.1- */
}
.iconfont {
  font-family:"iconfont" !important;
  font-size:16px;
  font-style:normal;
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-width: 0.2px;
  -moz-osx-font-smoothing: grayscale;
}
.top-bar {
  height: 65px;
  background-color: #282828;
  .top-wrapper {
    flex: 1;
    margin-right: 10px;
  }
  .new-message {
    padding: 16px 10px;
    height: 100%;
    float: right;
    .new-message-button {
      margin-bottom: 4px;
      background-size: cover;
    }
  }
  .search-area {
    padding: 16px 10px;
    height: 100%;
    max-width: 320px;
    float: right;
    .el-form-item {
      margin: 0;
      border-radius: 16px;
      .el-icon-search {
        top: 0;
        right: 0;
        font-size: 20px;
        position: absolute;
        z-index: 1;
        width: 32px;
        line-height: 32px;
        border-radius: 16px;
        text-align: center;
        background-color: #505050;
      }
    }
    .el-form-item__content {
      line-height: 1;
    }
    .el-input {
      position: relative;
      height: 32px;
      input {
        height: 32px;
        border: none;
        float: right;
        color: #E8E8E8;
        opacity: 1;
        border-radius: 16px;
        background-color: #505050;
        &::-webkit-input-placeholder {
          color: #E8E8E8;
        }
        &::-moz-placeholder {
          color: #E8E8E8;
        }
        &::-ms-input-placeholder {
          color: #E8E8E8;
        }
      }
    }
  }
  .user-area {
    padding: 16px 10px;
    display: inline-block;
    position: relative;
    &:hover {
      background-color: #505050;
      .avatar-drop-menu {
        display: block;
      }
    }
    .user-avatar {
      height: 32px;
      .avatar-img {
        display: inline-block;
        width: 32px;
        height: 32px;
        border-radius: 16px;
        margin-bottom: 4px;
        background: center no-repeat;
        background-size: cover;
        background-color: #505050;
      }
    }
  }
  .new-message-area {
    padding: 16px 10px;
    display: inline-block;
    position: relative;
    &:hover {
      background-color: #505050;
      .new-message-drop-menu {
        display: block;
      }
    }
  }
  .avatar-drop-menu {
    position: absolute;
    right: 0;
    top: 64px;
    display: none;
    width: 120px;
    z-index: 4;
    color: #E8E8E8;
    background-color: #505050;
    box-shadow: 0 5px 10px #505050;
    ul {
      list-style: none;
      margin: 0;
      padding: 0;
    }
    li {
      padding: 12px 20px;
      cursor: pointer;
      line-height: 1;
      font-size: 14px;
      &:hover {
        color: #00CCFF;
      }
    }
    .iconfont {
      font-size: 20px;
      margin-right: 10px;
    }
  }
  .new-message-drop-menu {
    position: absolute;
    right: 0;
    top: 64px;
    display: none;
    width: 300px;
    z-index: 4;
    color: #E8E8E8;
    background-color: #505050;
    box-shadow: 0 5px 10px #505050;
    ul {
      list-style: none;
      margin: 0;
      padding: 0;
    }
    li {
      padding: 12px 20px;
      cursor: pointer;
      line-height: 18px;
      font-size: 14px;
      &:hover {
        color: #00CCFF;
      }
    }
  }
}
</style>
