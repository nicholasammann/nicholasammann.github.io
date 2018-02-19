---
title:  Drag and Drop Object Instantiation with Qt5
date:   2018-02-19
cover:  /media/simblee_cover.jpg
thumb:  /media/simblee_thumb.jpg

---

This is an example sentence for drag and drop object instantiation blog post.  I'm going to write about archetypes and models as game objects in the Yours Truly Engine.

<!--more-->

Here's a a lot more writing about how I did drag and drop. Here's a a lot more writing about how I did drag and drop. Here's a a lot more writing about how I did drag and drop. Here's a a lot more writing about how I did drag and drop.


## Overwriting Drag and Drop Events on the Receiving Widget

{% highlight C++ %}
void ComponentTree::dropEvent(QDropEvent *aEvent)
  {
    QObject *sourceObj = aEvent->source();

    ObjectBrowser *objBrowser = dynamic_cast<ObjectBrowser*>(sourceObj);

    if (objBrowser)
    {
      aEvent->ignore();
    }

    FileViewer *fileViewer = dynamic_cast<FileViewer*>(sourceObj);

    if (fileViewer)
    {
      const QMimeData *rawData = aEvent->mimeData();

      QByteArray encodedData = rawData->data("application/vnd.text.list");
      QDataStream stream(&encodedData, QIODevice::ReadOnly);
      QStringList newItems;

      int rows = 0;

      while (!stream.atEnd())
      {
        QString text;
        stream >> text;
        newItems << text;
        ++rows;
      }

      std::string filename = newItems[0].toStdString();

      QTreeWidgetItem *item = this->itemAt(aEvent->pos());
      QWidget *widget = this->itemWidget(item->child(item->childCount() - 1), 0);

      ComponentWidget *componentWidget = static_cast<ComponentWidget*>(widget);
      
      YTE::Component *component = componentWidget->GetEngineComponent();
      YTE::Animator *animator = static_cast<YTE::Animator*>(component);
      YTE::Animation *animation = animator->AddAnimation(filename);

      if (animation == nullptr)
      {
        aEvent->ignore();
        return;
      }

      LoadGameObject(animator->GetOwner());
    }

    aEvent->ignore();
  }

  void ComponentTree::dragEnterEvent(QDragEnterEvent *aEvent)
  {
    aEvent->acceptProposedAction();
  }

  void ComponentTree::dragMoveEvent(QDragMoveEvent *aEvent)
  {
    QTreeWidgetItem *item = this->itemAt(aEvent->pos());
    
    // check if the cursor is hovering over an item
    if (item)
    {
      QWidget *widget = this->itemWidget(item, 0);

      // check if the cursor is hovering over the body of the component
      if (!widget)
      {
        QString itemText = item->text(0);

        if (item->text(0) == "Animator")
        {
          aEvent->acceptProposedAction();
          return;
        }
      }
    }

    aEvent->setAccepted(false);
  }
{% endhighlight %}