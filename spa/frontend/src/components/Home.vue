<template>
  <div>
    <div class="imgContent">
      <div class="imagePreview">
        <img :src="uploadedImage" style="width:100%;" />
      </div>
      <input type="file" class="file_input" name="photo" @change="onFileChange"  accept="image/*" />
      <button @click='onUploadImage'>Please judge the image ...</button>
      <ul id="response">
        <li v-for="item in modelResponse" :key="item.classe">
          {{ item.classe }}
        </li>
      </ul>
    </div>
  </div>
</template>


<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'
export default {
  data () {
    return {
      uploadedImage: '',
      modelResponse: ''
    }
  },
  methods: {
    //Reflect the selected image
    onFileChange (e) {
      let files = e.target.files || e.dataTransfer.files
      this.createImage(files[0])
    },
    //View uploaded image
    createImage (file) {
      let reader = new FileReader()
      reader.onload = (e) => {
        this.uploadedImage = e.target.result
      }
      reader.readAsDataURL(file)
    },
    //Upload image to server
    onUploadImage () {
      var params = new FormData()
      params.append('image', this.uploadedImage)
      //I am posting the data converted to FormData using Axios to Flask.
      axios.post(`${API_URL}/classification`, params).then(function (response) {
        this.modelResponse = response.data()
      })
    }
  }
}
</script>