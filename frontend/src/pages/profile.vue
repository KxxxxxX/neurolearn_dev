<template>
  <div>
    <div class="profile-area">
      <div class="profile-detail">
        <img style="float: left; height: auto; width: 200px" src="https://avatars2.githubusercontent.com/u/17725948?s=460&v=4">
        <div style="line-height: 30px">
          <span style="padding-left: 20px; font-family: Arial; font-weight: 200; font-size: 40px; color: #282828">Raniac</span><br/>
          <span style="padding-left: 20px; font-family: Arial; font-weight: 100; font-size: 20px; color: #505050">Master of Science from SCUT</span><br/>
          <span style="padding-left: 20px; font-family: Arial; font-weight: 100; font-size: 20px; color: #505050">Interests:  Artificial Intelligence & Neuro-Informatics</span><br/>
        </div>
        <div style="margin-top: 40px; line-height: 30px">
          <a class="github-link" href="https://github.com/Raniac" target="_blank">Paper: NEURO-LEARN</a><br/>
          <a class="github-link" href="https://github.com/Raniac" target="_blank">GitHub/Raniac</a><br/>
        </div>
      </div>
    </div>
    <div class="projects-area">
    <div>
      <h1 style="padding-left: 20px; font-family: Arial; font-weight: 150; font-size: 30px; color: #282828">Joined Projects</h1>
    </div>
    <div style="margin: 14px">
      <el-table
        class="projects-table"
        :data="projects_table"
        stripe
        border
        style="width: 100%; background-color: #E8E8E8; color: #282828; ">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" in-line class="demo-table-expand">
              <el-form-item label="Research Content">
                <span>{{ props.row.research_content }}</span>
              </el-form-item>
              <el-form-item label="Feature Types">
                <span>{{ props.row.feat_types }}</span>
              </el-form-item>
              <el-form-item label="Data Size">
                <span>{{ props.row.data_size }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column
        label="Project ID"
        prop="project_id">
        </el-table-column>
        <el-table-column
        label="Project Name"
        prop="project_name">
        </el-table-column>
        <el-table-column
        label="Status"
        prop="project_status">
        </el-table-column>
      </el-table>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      search_input: '',
      selected_status: '',
      projects_table: [{
        project_id: '2019050501',
        project_name: 'AD_with_sMRI',
        project_status: 'active',
        research_content: 'Using NiPype to calculate GMV, CT and CA, predict AD.',
        feat_types: 'Gray Matter Volume, Cortical Thickness, Cortical Area.',
        data_size: '1000'
      }, {
        project_id: '2019050502',
        project_name: 'SZ_with_fMRI',
        project_status: 'active',
        research_content: 'Using NiLearn to calculate FC, DC and CC, predict SZ.',
        feat_types: 'Functional Connectivity, Degree Centrality, Clustering Coefficient.',
        data_size: '954'
      }, {
        project_id: '2019050503',
        project_name: 'SZ_with_s/fMRI',
        project_status: 'active',
        research_content: 'Fusing multi-modal data, using NiLearn to calculate GMV and FC, predict SZ.',
        feat_types: 'Gray Matter Volume, Functional Connectivity.',
        data_size: '675'
      }]
    }
  }
}
</script>

<style lang="scss">
.profile-area {
  margin: 14px;
  padding: 14px;
  background-color: #FFFFFF;
  .profile-detail {
    padding: 14px;
    min-height: 200px;
    .github-link {
      padding-left: 20px;
      font-family: Arial;
      font-weight: 100;
      font-size: 20px;
      color: #282828;
      &:hover {
      color: #00CCFF;
      }
    }
  }
}
.projects-area {
  margin: 14px;
  padding: 14px;
  background-color: #FFFFFF;
}
.input-with-select .el-input-group__prepend {
  background-color: #FFFFFF;
  .el-select .el-input {
    width: 130px;
}
}
.demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 140px;
    color: #505050;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 100%;
  }
</style>
