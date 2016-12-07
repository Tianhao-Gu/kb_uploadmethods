
package us.kbase.kbuploadmethods;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: inputParamUploadFile</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "fastq_file_path",
    "secondary_fastq_file_path",
    "reads_file_name"
})
public class InputParamUploadFile {

    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("fastq_file_path")
    private String fastqFilePath;
    @JsonProperty("secondary_fastq_file_path")
    private String secondaryFastqFilePath;
    @JsonProperty("reads_file_name")
    private String readsFileName;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public InputParamUploadFile withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("fastq_file_path")
    public String getFastqFilePath() {
        return fastqFilePath;
    }

    @JsonProperty("fastq_file_path")
    public void setFastqFilePath(String fastqFilePath) {
        this.fastqFilePath = fastqFilePath;
    }

    public InputParamUploadFile withFastqFilePath(String fastqFilePath) {
        this.fastqFilePath = fastqFilePath;
        return this;
    }

    @JsonProperty("secondary_fastq_file_path")
    public String getSecondaryFastqFilePath() {
        return secondaryFastqFilePath;
    }

    @JsonProperty("secondary_fastq_file_path")
    public void setSecondaryFastqFilePath(String secondaryFastqFilePath) {
        this.secondaryFastqFilePath = secondaryFastqFilePath;
    }

    public InputParamUploadFile withSecondaryFastqFilePath(String secondaryFastqFilePath) {
        this.secondaryFastqFilePath = secondaryFastqFilePath;
        return this;
    }

    @JsonProperty("reads_file_name")
    public String getReadsFileName() {
        return readsFileName;
    }

    @JsonProperty("reads_file_name")
    public void setReadsFileName(String readsFileName) {
        this.readsFileName = readsFileName;
    }

    public InputParamUploadFile withReadsFileName(String readsFileName) {
        this.readsFileName = readsFileName;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((("InputParamUploadFile"+" [workspaceName=")+ workspaceName)+", fastqFilePath=")+ fastqFilePath)+", secondaryFastqFilePath=")+ secondaryFastqFilePath)+", readsFileName=")+ readsFileName)+", additionalProperties=")+ additionalProperties)+"]");
    }

}