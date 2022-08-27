<template>
  <div class="home">
    <p class="title is-1">农历生日提醒</p>
    <div class="birthday-card">
      <div class="panel">
        <p class="panel-heading">任务列表</p>
        <div class="panel-block flex-between">
          <!-- add new -->
          <span class="new-btn" @click="openCreateModal">
            <b-icon icon="plus"></b-icon>
          </span>
          <!-- search -->
          <b-field class="search-bar">
            <b-input
              class="search-i"
              v-model="username"
              placeholder="输入用户名..."
              type="search"
              @keyup.native.enter="getBirthdayByUsername"
              icon="magnify"
              expanded
            >
            </b-input>
            <p class="control">
              <b-button
                type="is-primary"
                label="搜索"
                @click="getBirthdayByUsername"
              />
            </p>
          </b-field>
        </div>
        <!-- no search result -->
        <a class="no-result panel-block" v-if="tasks.length == 0">
          <span>
            <span>
              <b-icon type="is-danger" icon="alert-decagram"> </b-icon>
            </span>
            无内容
          </span>
        </a>
        <!-- result -->
        <a v-if="tasks.length != 0">
          <a
            v-for="(item, i) in tasks"
            :key="i"
            class="panel-block flex-between"
          >
            <span>
              <span>
                <b-icon icon="calendar-check"> </b-icon>
              </span>
              在 {{ item[1] }}
              傳送到{{ item[2] }}的生日。
            </span>

            <span class="buttons">
              <b-button
                type="is-danger"
                icon-left="delete"
                @click.stop="openDeleteModal(item)"
              >
                删除
              </b-button>
            </span>
          </a>
        </a>
      </div>
    </div>
    <!-- {{tasks}} -->
    <!-- add task modal -->
    <b-modal
      v-model="isCreateModalActive"
      has-modal-card
      trap-focus
      :destroy-on-hide="false"
      aria-role="dialog"
    >
      <div class="card">
        <div class="card-content">
          <!-- username -->
          <b-field label="用戶名">
            <b-input v-model="newTask.username"></b-input>
          </b-field>
          <!-- birthday_time -->
          <b-field label="对方生日日期，格式：月-日（例3-1 是3月1日）">
            <b-input v-model="newTask.birthday_time"></b-input>
          </b-field>

          <!-- to_user -->
          <b-field label="需要被提醒人的名字">
            <b-input v-model="newTask.to_user"></b-input>
          </b-field>

          <div class="end-button">
            <div class="buttons">
              <b-button
                type="is-danger"
                @click="isCreateModalActive = false"
                outlined
                >取消</b-button
              >
              <b-button type="is-success" @click="taskAdd">新增</b-button>
            </div>
          </div>
        </div>
      </div>
    </b-modal>
    <!-- delete task modal -->
    <b-modal
      v-model="isDeleteModalActive"
      has-modal-card
      trap-focus
      :destroy-on-hide="false"
      aria-role="dialog"
    >
      <div class="card">
        <div class="card-content">
          <div>
            <p class="title is-4">你确定要删除这个任务吗？</p>
          </div>
          <p type="is-info">
              在 {{ deleteTask[1] }}
              傳送到{{ deleteTask[2] }}的生日。
          </p>
          <div class="end-button">
            <div class="buttons">
              <b-button
                type="is-success"
                @click="isDeleteModalActive = false"
                outlined
                >取消</b-button
              >
              <b-button type="is-danger" @click="taskDelete">删除</b-button>
            </div>
          </div>
        </div>
      </div>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "Home",
  components: {},
  data() {
    return {
      username: "",
      tasks: [],
      newTask: {},
      deleteTask: [],
      isCreateModalActive: false,
      isDeleteModalActive: false,
    };
  },
  created() {
    this.initNewTask();
  },
  methods: {
    openCreateModal() {
      this.isCreateModalActive = true;
      this.initNewTask();
      this.newTask.username = this.username;
    },
    openDeleteModal(task) {
      this.isDeleteModalActive = true;
      this.deleteTask = task;
    },
    initNewTask() {
      this.newTask = {
        username: "",
        birthday_time: "",
        hour: "",
        minute: "",
        to_user: "",
        email: "",
      };
    },

    async getBirthdayByUsername() {
      axios
        .get(this.baseURL + this.birthdayURL + this.username)
        .then((response) => {
          // console.log(response);
          // console.log(response.data);
          let res = response.data.data;
          this.tasks = [];
          for (var task in res.tasks) {
            this.tasks.push(res.tasks[task]);
          }
          console.log(this.tasks);
          this.$buefy.toast.open({
            message: "获取任务列表成功",
            type: "is-success",
          });
        })
        .catch((error) => {
          console.log(error);
          this.$buefy.toast.open({
            message: "获取任务列表失败",
            type: "is-danger",
          });
        });
    },

    async taskAdd() {
      let data = new FormData();
      data.append("username", this.newTask.username);
      data.append("birthday_time", this.newTask.birthday_time);
      data.append("hour", this.newTask.hour);
      data.append("minute", this.newTask.minute);
      data.append("to_user", this.newTask.to_user);
      data.append("email", this.newTask.email);

      // 做空值判断处理
      if( this.newTask.username &&
          this.newTask.birthday_time &&
          this.newTask.to_user
      ){
      }else{
          this.$buefy.toast.open({
            message: "信息中含有非法值",
            type: "is-danger",
          });
          return;
      }

      axios
        .post(this.baseURL + this.taskAddURL, data, {
          headers: { "Content-Type": "form-data" },
          transformRequest: [(data, headers) => data], //預設值，不做任何轉換
        })
        .then((response) => {
          console.log(response);
          console.log(response.data);
          this.isCreateModalActive = false;
          this.initNewTask();
          this.$buefy.toast.open({
            message: "添加任务成功",
            type: "is-success",
          });
        })
        .catch((error) => {
          console.log(error);
          this.$buefy.toast.open({
            message: "添加任务失败",
            type: "is-danger",
          });
        });
    },

    async taskDelete() {
      this.isDeleteModalActive = false;
      let data = new FormData();
      data.append("username", this.deleteTask[2]);
      data.append("task_id", this.deleteTask[0]);
      axios
        .post(this.baseURL + this.taskDeleteURL, data, {
          headers: { "Content-Type": "form-data" },
          transformRequest: [(data, headers) => data], //預設值，不做任何轉換
        })
        .then((response) => {
          console.log(response);
          console.log(response.data);
          for (let index = 0; index < this.tasks.length; index++) {
            if (this.tasks[index][0] === this.deleteTask[0]) {
              this.tasks.splice(index, 1);
            }
          }
          this.$buefy.toast.open({
            message: "删除任务成功",
            type: "is-success",
          });
        })
        .catch((error) => {
          console.log(error);
          this.$buefy.toast.open({
            message: "删除任务失败",
            type: "is-danger",
          });
        });
    },
  },
  computed: {
    ...mapState({
      baseURL: (state) => {
        return state.api.baseURL;
      },
      birthdayURL: (state) => {
        return state.api.birthdayURL;
      },
      taskAddURL: (state) => {
        return state.api.taskAddURL;
      },
      taskDeleteURL: (state) => {
        return state.api.taskDeleteURL;
      },
    }),
  },
};
</script>

<style>
.birthday-card {
  padding-top: 10%;
  padding-left: 20%;
  padding-right: 20%;
}
.flex-between {
  display: flex;
  justify-content: space-between !important;
}
.title {
  padding: 1rem;
  text-align: center;
}
.no-result {
  display: flex;
  justify-content: center !important;
  height: 5rem;
}
.end-button {
  display: flex;
  justify-content: flex-end;
}
.new-btn {
  text-align: center;
  padding: 0.5rem !important;
  border-radius: 50%;
  background-color: white;
}
.new-btn:hover {
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  box-shadow: 2px 2px 4px 4px rgba(0, 0, 0, 0.1);
}
.search-i {
  text-align: center;
}
</style>