<template>
  <div>
    <div class="imgContent">
      <div class="imagePreview">
        <img :src="uploadedImage" style="width:30%;" />
      </div>
      <input type="file" class="file_input" name="photo" @change="onFileChange"  accept="image/*" />
      <button @click='onUploadImage'>Please judge the image ...</button>
    </div>
    <ul id="resultModel">
        {{ modelResponse }}
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'
export default {
  data () {
    return {
      uploadedImage: '',
      modelResponse: null
    }
  },
  methods: {
    // Reflect the selected image
    onFileChange (e) {
      let files = e.target.files || e.dataTransfer.files
      this.createImage(files[0])
    },
    // View uploaded image
    createImage (file) {
      let reader = new FileReader()
      reader.onload = (e) => {
        this.uploadedImage = e.target.result
      }
      reader.readAsDataURL(file)
    },
    // Upload image to server
    onUploadImage () {
      var params = new FormData()
      params.append('image', this.uploadedImage)
      // I am posting the data converted to FormData using Axios to Flask.
      axios.post(`${API_URL}/classification`, params)
        .then(res => {
          console.log(res)
          this.modelResponse = res.data.response
        })
    }
  }
}
</script>
