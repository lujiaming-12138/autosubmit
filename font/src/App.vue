<template>
  <div id="app">
    <form>
      <div class="input">
        <label for="username">账号</label>
        <input type="text" id="username"  autofocus v-model="username">
      </div>
      <div class="input">
        <label for="password">密码</label>
        <input type="text" id="password" v-model="password">
      </div>
      <div class="input">
        <label for="email">邮箱</label>
        <input type="text" id="email" v-model="email">
      </div>
      <div class="input">
        <label>地址</label>
        <textarea readonly>{{location == '' ? '' : JSON.parse(location).formattedAddress}}</textarea>
      </div>
      <div class="input">
        <input type="button" value="提交" @click="submit">
      </div>
    </form>
  </div>
</template>

<script>

export default {
  name: 'App',
  props: {
    location: String
  },
  data() {
    return {
      username: '',
      password: '',
      email: ''
    }
  },
  methods: {
    submit() {
      this.axios.post('https://2239559319.pythonanywhere.com/autosubmit', {
        username: this.username,
        password: this.password,
        email: this.email,
        location: this.location
      })
      .then(v => v.data)
      .then(v => {
        console.log(v)
        if(v.msg == 'duplicate') {
          alert('用户已经输入过信息，无需再次输入')
        } else if(v.msg == 'success') {
          alert('提交成功,请等待邮件')
        }
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.input{
  height: 10vh;
}
input[type="text"]{
  margin-left: 3rem;
}
textarea{
  margin-left: 3rem;
  outline: none;
}
input[type="button"]{
  width: 4rem;
  height: 2.5rem;
}
</style>
