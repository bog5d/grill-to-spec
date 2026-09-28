# Remote Repository Creation

建议远端：`bog5d/grill-to-spec`

建议初始 visibility：public（只放通用方法、模板、示例，不得放公司真实机密、人员评价、密钥）。

创建远端后：

```bash
git remote add origin git@github.com:bog5d/grill-to-spec.git
git push -u origin main
```

如决定先私有试运行，也可以先 private；方法成熟后再单独清理/审计后公开。
