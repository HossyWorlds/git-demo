# Cherry-pick手順ガイド

## 概要
stagingブランチにマージされた複数の機能から、特定の機能（feature/A）のみをmainブランチに反映する方法

## 前提条件
- stagingブランチ: feature/AとFeature/Bの両方の変更を含む
- mainブランチ: 本番環境（初期状態）
- 目標: feature/Aの変更のみをmainに適用

## 手順

### 1. 対象コミットの特定
```bash
# stagingブランチのコミット履歴を確認
git log --oneline staging

# または、特定の機能名でフィルタリング
git log --oneline staging | grep "Feature A"
```

### 2. mainブランチに切り替え
```bash
git checkout main
```

### 3. cherry-pickの実行
```bash
# コミットハッシュを指定してcherry-pick
git cherry-pick <commit-hash>

# 例：Feature Aのコミットを適用
git cherry-pick 95d2674
```

### 4. 結果の確認
```bash
# ファイルの確認
ls -la

# 変更内容の確認
git status
git log --oneline

# アプリケーションの動作確認
python app.py
```

## 注意事項
- cherry-pickは指定したコミットの変更のみを適用します
- コンフリクトが発生した場合は手動で解決が必要です
- 複数のコミットを適用する場合は、順番に注意してください

## トラブルシューティング

### コンフリクトが発生した場合
```bash
# コンフリクトを確認
git status

# ファイルを編集してコンフリクトを解決
# 解決後、cherry-pickを継続
git add <resolved-files>
git cherry-pick --continue

# またはcherry-pickを中止
git cherry-pick --abort
```
