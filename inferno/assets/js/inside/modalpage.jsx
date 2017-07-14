import React from 'react'
import { Button, Header, Icon, Image, Modal } from 'semantic-ui-react'

const Modalpage = () => (
  <Modal trigger={<Button>參與評比該課程</Button>}>
    <Modal.Header>評比問卷</Modal.Header>
    <Modal.Content image>
      <Image wrapped size='medium' src='/assets/images/wireframe/image.png' />
      <Modal.Description>
        <Header>Modal Header</Header>
        <p>This is an example of expanded content that will cause the modals dimmer to scroll</p>
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
        <Image src='/assets/images/wireframe/paragraph.png' />
      </Modal.Description>
    </Modal.Content>
    <Modal.Actions>
      <Button primary>
        Proceed <Icon name='right chevron' />
      </Button>
    </Modal.Actions>
  </Modal>
)

export default Modalpage