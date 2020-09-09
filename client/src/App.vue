<template>
  <v-app id="sandbox">
    <v-app-bar app>
      <v-toolbar-title>F-Secure</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-card height="100%">
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="8" offset="2">
                <template v-if="feedMessages.length == 0">
                  <p>
                    Your Feed is Empty.. <br />
                    Press the <code>+</code> sign to add a message
                  </p>
                </template>
                <template v-else>
                  <v-card
                    class="mb-2"
                    v-for="(message, index) in feedMessages"
                    :key="index"
                  >
                    <v-card-title>
                      {{ message.title }}
                    </v-card-title>
                    <v-card-subtitle>
                      {{ message.sender }}
                    </v-card-subtitle>
                    <v-card-text>
                      {{ message.content }}
                    </v-card-text>
                    <v-card-actions>
                      {{ message.url }}
                    </v-card-actions>
                  </v-card>
                </template>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-dialog width="500" v-model="dialogOpen">
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" color="pink" dark small absolute bottom right fab>
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </template>

          <v-card>
            <v-card-title class="headline grey lighten-2">
              Create Message
            </v-card-title>

            <v-card-text>
              <v-text-field
                autofocus
                :rules="rules.required"
                v-model="newMessage.title"
                label="title"
              ></v-text-field>
              <v-textarea
                :rules="rules.required"
                clearable
                auto-grow
                rows="1"
                v-model="newMessage.content"
                label="content"
              ></v-textarea>
              <v-text-field
                :rules="rules.required"
                v-model="newMessage.sender"
                label="sender"
              ></v-text-field>
              <v-text-field
                v-model="newMessage.url"
                label="url (optional)"
              ></v-text-field>
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="primary"
                text
                @click="
                  dialog = false;
                  CreateMessage();
                "
              >
                Create
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-card>
    </v-main>

    <v-footer inset app>
      <span class="px-4">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import axios from "axios";

const url = "http://localhost:8000/api";
export default {
  data() {
    return {
      dialogOpen: false,
      rules: {
        required: [(value) => !!value || "required"],
      },
      newMessage: {
        title: "",
        content: "",
        sender: "",
        url: "",
      },
      feedMessages: [],
    };
  },
  methods: {
    async CreateMessage() {
      if (
        !this.newMessage.title ||
        !this.newMessage.content ||
        !this.newMessage.sender
      )
        return;
      const reply = await axios.post(`${url}/CreateMessage/`, this.newMessage);
    },
    async RequestMessagesList() {
      return axios.get(`${url}/ListMessages/`);
    },
  },
  watch: {
    dialogOpen(state) {
      if (state) {
        this.newMessage.title = undefined;
        this.newMessage.content = undefined;
        this.newMessage.sender = undefined;
        this.newMessage.url = undefined;
      }
    },
  },
};
</script>
